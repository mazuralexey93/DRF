import './App.css';
import React from 'react';
import UsersList from "./components/Users";
import axios from "axios";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        };
    }

    componentDidMount() {
        // const users = [
        //     {
        //         'username': 'Doctor',
        //         'first_name': 'Johny',
        //         'last_name': 'Four fingers',
        //         'email': 'no_finger@mail.com'
        //     },
        //     {
        //         'username': 'Bell',
        //         'first_name': 'Kate',
        //         'last_name': 'Cute',
        //         'email': 'catarsys@mail.com'
        //     }
        // ]
        // this.setState(this.state = {
        //         'users': users
        //     }
        // )


        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data;
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))
    }


    render() {
        return (
            <div>
                <UsersList users={this.state.users}/>
            </div>

        )
    }
}


export default App;
