import './App.css';
import React from 'react';
import UsersList from "./components/Users";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        };
    }

    componentDidMount() {
        const users = [
            {
                'username': 'Doctor',
                'first_name': 'Johny',
                'last_name': 'Four fingers',
                'email': 'no_finger@mail.com'
            },
            {
                'username': 'Bell',
                'first_name': 'Kate',
                'last_name': 'Cute',
                'email': 'catarsys@mail.com'
            }
        ]

        this.setState(
            this.state = {
                'users': users
            }
        )
    }

    render() {
        return (

            // <UserItem user={{
            //     'username': 'Doctor',
            //     'first_name': 'Johny',
            //     'last_name': 'Four fingers',
            //     'email': 'no_finger@mail.com'
            // }}/>
          <UsersList users={this.state.users}/>
        )
    }
}


export default App;
