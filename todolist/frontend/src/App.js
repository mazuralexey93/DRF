import './App.css';
import React from 'react';

import axios from "axios";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import UsersList from "./components/Users";
import ProjectsList from "./components/Projects";
import ToDosList from "./components/ToDos";
import ProjectInstance from "./components/ProjectInstance";

import {HashRouter, Route, Switch, Link, Redirect} from "react-router-dom";


const pageNotFound404 = ({location}) => {
    return (
        <h1> 404: Page '{location.pathname}' doesn't exist!</h1>
    )
}

const API_ROOT = 'http://127.0.0.1:8000/';
const getUrl = (name) => `${API_ROOT}${name}`;


class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': []
        }
    }

    componentDidMount() {
        axios
            .get(getUrl('api/users'))
            .then(response => {
                const users = response.data;
                this.setState({
                        users: users.results
                    }
                )
            })
            .catch(error => console.log(error))
        axios
            .get(getUrl('views/set/projects'))
            .then(response => {
                const projects = response.data;
                this.setState({
                        projects: projects.results
                    }
                )
            })
            .catch(error => console.log(error))
        axios
            .get(getUrl('views/set/todos'))
            .then(response => {
                const todos = response.data;
                this.setState({
                        todos: todos.results
                    }
                )
            })
            .catch(error => console.log(error))
    }


    render() {
        return (
            <div className={'App'}>
                <Menu/>
                <HashRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to={'/'}>Users</Link>
                            </li>
                            <li>
                                <Link to={'/projects/'}>Projects</Link>
                            </li>
                            <li>
                                <Link to={'/todos/'}>todos</Link>
                            </li>


                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path={'/'}
                               component={() => <UsersList users={this.state.users}/> } />
                        <Route exact path={'/projects/'}
                               component={() => <ProjectsList projects={this.state.projects} /> } />
                        <Route exact path={'/project/:id'}
                               component={() => <ProjectInstance projects={this.state.projects} /> } />
                        <Route exact path={'/todos/'}
                               component={() => <ToDosList todos={this.state.todos} /> } />
                        <Redirect from={'/users/'} to={'/'} />
                        <Route component={pageNotFound404} />
                    </Switch>
                </HashRouter>
                <Footer/>
            </div>
        );
    }
}


export default App;
