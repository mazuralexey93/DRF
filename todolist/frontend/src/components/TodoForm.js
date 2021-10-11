import React from 'react'


class TodoForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            text: "",
            project: 0,
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
        this.props.todoCreate(this.state.text, this.state.project, this.state.user);
    }


    render() {
        return (
            <form className="todoForm"
                  onSubmit={(event) => this.handlerOnSubmit(event)}>
                <input type="text" name="text" placeholder="text" value={this.state.text}
                       onChange={(event) => this.handlerOnChange(event)}/>
                <select name="user"
                        onChange={(event) => this.handlerOnChange(event)}>
                    {this.props.users.map((user) => (
                        <option value={user.id} key={user.id}>{user.first_name}{user.last_name}</option>
                    ))}
                </select>
                <select name="project"
                        onChange={(event) => this.handlerOnChange(event)}>
                    {this.props.projects.map((project) => (
                        <option value={project.id} key={project.id}>{project.name}</option>
                    ))}
                </select>
                <input type="submit" value="Create"/>
            </form>
        )
    }
}


export default TodoForm;