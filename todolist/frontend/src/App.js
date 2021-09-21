import './App.css';
import React from 'react';

import axios from "axios";
import Cookies from "universal-cookie/lib";
import {BrowserRouter, Route, Switch, Link, Redirect} from "react-router-dom";

import Menu from "./components/Menu";
import Footer from "./components/Footer";
import UsersList from "./components/Users";
import ProjectsList from "./components/Projects";
import ToDosList from "./components/ToDos";
import ProjectInstance from "./components/ProjectInstance";
import LoginForm from "./components/Auth";


const pageNotFound404 = ({location}) => {
    return (
        <h1> 404: Page '{location.pathname}' doesn't exist!</h1>
    )
}

const API_ROOT = 'http://127.0.0.1:8000/';
const getUrl = (name) => `${API_ROOT}${name}`;


class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'project': {},
            'token' : ''
        }
    }


    logout() {
        this.setToken('');
    }

    getToken(username, password) {
        axios.post(
            getUrl('api-token-auth/'),
            {username: username, password: password})
            .then(response => {
                this.setToken(response.data['token'])
            })
            .catch(error => alert('Неверный логин или пароль'))
    }

    getTokenFromStorage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        console.log("token", token)
        this.setState({'token': token}, () => this.loadData())
    }

    setToken(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.loadData())
    }

    loadData() {
        if (!this.isAuthenticated()) {
            return
        }
        const headers = this.getHeaders()
        axios
            .get(getUrl('api/users'), {headers})
            .then(response => {
                this.setState({users: response.data})
            })
            .catch(error => console.log(error))

        axios
            .get(getUrl('api/projects'), {headers})
            .then(response => {
                this.setState({projects: response.data})
            })
            .catch(error => {
                console.log(error)
                this.setState({'projects': []})
            })

        axios
            .get(getUrl('api/todos'), {headers})
            .then(response => {
                this.setState({todos: response.data})
            })
            .catch(error => {
                console.log(error)
                this.setState({'todos': []})
            })
    }

    getHeaders() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.isAuthenticated()) {
            headers['Authorization'] = `Token ${this.state.token}`;
            return headers
        }
    }

    isAuthenticated() {
        return this.state.token !== '';
    }

     getProject(id) {
        const headers = this.getHeaders()
        console.log('call', getUrl(`api/projects/${id}`))
        axios.get(getUrl(`api/projects/${id}`), {headers})
            .then(response => {
                this.setState({project: response.data})
                console.log(response.data)
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.getTokenFromStorage();
    }

    render() {
        return (
            <div className={'App'}>
                <Menu/>
                <BrowserRouter>
                    <nav className={'NavBar'}>
                        <ul>
                            <li>
                                <Link to={'/'}>Users</Link>
                            </li>
                            <li>
                                <Link to={'/projects'}>Projects</Link>
                            </li>
                            <li>
                                <Link to={'/todos'}>Todos</Link>
                            </li>
                            <li>
                                {this.isAuthenticated() ?
                                    <button onClick={() => this.logout()}>Logout</button> :
                                    <Link to={'/login'}>Login</Link>}

                            </li>
                        </ul>
                    </nav>

                    <Switch>
                        <Route exact path={'/'}
                               component={() => <UsersList users={this.state.users}/>}/>
                        <Route exact path={'/projects'}
                               component={() => <ProjectsList projects={this.state.projects}/>}/>
                        <Route path={'/projects/:id'}>
                            <ProjectInstance
                                getProject={(id) => this.getProject(id)}
                                             project={this.state.project}
                            getToken={(username, password) => this.getToken(username, password)}/>
                        </Route>
                        <Route exact path={'/login'}>
                            <LoginForm getToken={(username, password) => this.getToken(username, password)}/>
                        </Route>
                        <Route exact path={'/todos'}
                               component={() => <ToDosList todos={this.state.todos}/>}/>
                        <Redirect from={'/users'} to={'/'}/>
                        <Route component={pageNotFound404}/>
                    </Switch>
                </BrowserRouter>
                <Footer/>
            </div>
        );
    }
}


export default App;
