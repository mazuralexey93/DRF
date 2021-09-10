import './App.css';
import React from 'react';

import axios from "axios";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import UsersList from "./components/Users";
import ProjectsList from "./components/Projects";
import ToDosList from "./components/ToDos";



const API_ROOT = 'http://127.0.0.1:8000/api/';
const getUrl = (name) => `${API_ROOT}${name}`;

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        };
    }

    // componentDidMount() {
    //
    //     axios
    //         .get(getUrl('users'))
    //         .then(response => {
    //             const users = response.data;
    //             this.setState({
    //                     'users': users
    //                 }
    //             )
    //         })
    //         .catch(error => console.log(error))
    // }

    render() {
        return (
            <div>
                <Menu/>
                <UsersList users={this.state.users}/>
                <Footer/>
            </div>
        );
    }
}


export default App;
