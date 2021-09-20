import React from 'react'


class LoginForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            password: ""
        }
    }

    handlerOnChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handlerOnSubmit(event) {
        this.props.getToken(this.state.username, this.state.password);
        event.preventDefault();
    }


    render() {
        return (
            <form className="loginForm"
                  onSubmit={(event) => this.handlerOnSubmit(event)}>
                <input type="text" name="username" placeholder="username"
                       onChange={(event) => this.handlerOnChange(event)}/>
                <input type="password" name="password" placeholder="password"
                       onChange={(event) => this.handlerOnChange(event)}/>
                <input type="submit" value="login"/>
            </form>
        )
    }
}


export default LoginForm;