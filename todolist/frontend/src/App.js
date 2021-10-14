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
import ProjectForm from "./components/ProjectForm";
import TodoForm from "./components/TodoForm";


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
            'token': '',
            'search_todos': [],
            'search_projects': [],
            searchText: '',

        }
    }

    projectSearch(text) {
        let filteredProjects = this.state.search_projects
        if (text !== '') {
            filteredProjects = filteredProjects.filter((item) => item.name.includes(text))
        }
        this.setState({projects: filteredProjects})
    }

    todoSearch(text) {
        let filteredTodos = this.state.search_todos
        if (text !== '') {
            filteredTodos = filteredTodos.filter((item) => item.name.includes(text))
        }
        this.setState({todos: filteredTodos})
    }

    searchTextChange(text) {
        this.setState({'searchText': text})
        this.projectSearch(text)
    }

    findProjects() {
        console.log('Find:', this.state.searchText)
        let headers = this.getHeaders()
        let url = '/api/projects/';
        if (this.state.searchText !== '') {
            url = `/api/projects/?name=${this.state.searchText}`
        }
        console.log(url);
        axios.get(getUrl(url), {headers})
            .then(response => {
                this.setState({projects: response.data.result})
            }).catch(error => console.log(error))
    }

    logout() {
        this.setToken('');
    }

    getToken(username, password) {
        axios.post(
            getUrl('api/token-auth/'),
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
                this.setState({users: response.data.results})
            })
            .catch(error => console.log(error))

        axios
            .get(getUrl('api/projects'), {headers})
            .then(response => {
                this.setState({projects: response.data.results})
            })
            .catch(error => {
                console.log(error)
                this.setState({'projects': []})
            })

        axios
            .get(getUrl('api/todos'), {headers})
            .then(response => {
                this.setState({todos: response.data.results})
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

    projectDelete(id) {
        const headers = this.getHeaders()
        axios
            .delete(getUrl(`api/projects/${id}/`), {headers})
            .then(result => {
                this.setState({
                    projects: this.state.projects.filter((item) => item.id !== id)
                })
            })
            .catch(error => console.log(error))
    };

    projectCreate(name, user) {
        const headers = this.getHeaders()
        const data = {name: name, user: user}
        axios
            .post(getUrl('api/projects/'),
                {data},
                {headers})
            .then(result => {
                const newProject = result.data;
                this.setState({
                    projects: [...this.state.projects, newProject]
                })
            })
            .catch(error => console.log(error))
    }

    todoDelete(id) {
        const headers = this.getHeaders()
        axios
            .delete(getUrl(`api/todos/${id}/`), {headers})
            .then(result => {
                this.setState({
                    todos: this.state.todos.filter((item) => item.id !== id)
                })
            })
            .catch(error => console.log(error))
    };

    todoCreate(text, project, user) {
        const headers = this.getHeaders()
        axios
            .post(getUrl('api/todos/'),
                {text: text, project: project, user: user},
                {headers})
            .then(result => {
                const newTodo = result.data;
                this.setState({
                    todos: [...this.state.todos, newTodo]
                })
            })
            .catch(error => console.log(error))
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
                            <li>
                                <input type="text" placeholder="Search..."
                                       onChange={(event) =>
                                            this.searchTextChange(event.target.value)}/>
                                <button onClick={this.findProjects}>Search</button>
                            </li>
                        </ul>
                    </nav>

                    <Switch>
                        <Route exact path={'/'}
                               component={() => <UsersList users={this.state.users}/>}/>
                        <Route exact path={'/projects'}
                               component={() => <ProjectsList users={this.state.users}
                                                              projects={this.state.projects}
                                                              projectDelete={(id) => this.projectDelete(id)}
                                                              searchTextChange={(text) => this.searchTextChange(text)}
                                                              projectSearch={() => this.findProjects()}/>}/>

                        <Route exact path={'/projects/create'}
                               component={() => <ProjectForm
                                   users={this.state.users}
                                   projectCreate={(name, user) => this.projectCreate(name, user)}/>}/>
                        <Route exact path={'/projects/:id'}
                               component={() => <ProjectInstance getProject={(id) => this.getProject(id)}
                                                                 project={this.state.project}/>}/>
                        <Route exact path={'/todos'}
                               component={() => <ToDosList todos={this.state.todos}
                                                           users={this.state.users}
                                                           projects={this.state.projects}
                                                           todoDelete={(id) => this.todoDelete(id)}/>}/>
                        <Route exact path={'/todos/create'}
                               component={() => <TodoForm
                                   users={this.state.users}
                                   projects={this.state.projects}
                                   todoCreate={(text, project, user) => this.todoCreate(text, project, user)}/>}/>
                        <Route exact path={'/login'}
                               component={() => <LoginForm
                                   getToken={(username, password) => this.getToken(username, password)}/>}/>
                        <Route component={pageNotFound404}/>
                        <Redirect from={'/users'} to={'/'}/>
                    </Switch>
                </BrowserRouter>
                <Footer/>
            </div>
        )
            ;
    }
}


export default App;
