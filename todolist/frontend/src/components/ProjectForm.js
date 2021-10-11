import React from 'react'


class ProjectForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name: "",
            user: 0
        }
    }

    handlerOnChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handlerOnSubmit(event) {
        event.preventDefault();
        this.props.projectCreate(this.state.name, this.state.user);
    }


    render() {
        return (
            <form className="loginForm"
                  onSubmit={(event) => this.handlerOnSubmit(event)}>
                <input type="text" name="name" placeholder="name" value={this.state.name}
                       onChange={(event) => this.handlerOnChange(event)}/>
                <select name="user"
                    onChange={(event) => this.handlerOnChange(event)}>
                    {this.props.users.map((user) => (
                        <option value={user.id} key={user.id}>{user.first_name}{user.last_name}</option>
                    ))}
                </select>
                <input type="submit" value="Create"/>
            </form>
        )
    }
}


export default ProjectForm;