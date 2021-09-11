import './App.css';
import React from 'react';

// import axios from "axios";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import UsersList from "./components/Users";
import ProjectsList from "./components/Projects";
import ToDosList from "./components/ToDos";

import {HashRouter, Route} from "react-router-dom";


// const API_ROOT = 'http://127.0.0.1:8000/api/';
// const getUrl = (name) => `${API_ROOT}${name}`;


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': []

        };
    }

    // componentDidMount() {
    //
    //     axios
    //         // .get(getUrl('users', 'projects', 'todos'))
    //         .get(getUrl('users'))
    //         .then(response => {
    //             const users = response.data;
    //             const projects = response.data;
    //             const todos = response.data;
    //             this.setState({
    //                     'users': users
    //                     // 'users': users,
    //                     // 'projects': projects,
    //                     // 'todos': todos
    //                 }
    //             )
    //         })
    //         .catch(error => console.log(error))
    // }

    render() {
        return (
            <div className={'App'}>
                <Menu/>
                <HashRouter>
                    <Route exact path={'/'}
                           component={() => <UsersList users={this.state.users}/>}/>
                    <Route exact path={'/projects/'}
                        component={() => <ProjectsList projects={this.state.projects}/>}/>
                    <Route exact path={'/todos/'}
                        component={() => <ToDosList todos={this.state.todos}/>}/>
                </HashRouter>
                <Footer/>
            </div>
        );
    }
}


export default App;
