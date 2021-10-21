import React from 'react';
import {Link} from "react-router-dom";

const ToDoItem = ({todo, todoDelete}) => {
    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.text}</td>
            <td>{todo.project}</td>
            <td>{todo.created_at}</td>
            <td>{todo.user}</td>
            <td>{todo.updated_at}</td>
            <td>{todo.status}</td>
            <td>
                <button onClick={() => todoDelete(todo.id)}>
                    Delete
                </button>
            </td>
        </tr>
    );
};

const ToDosList = ({todos, todoDelete}) => {
    return (
        <div className="todos-list">
            <table className='table'>
                <thead>
                <tr>
                    <th>TODOS</th>
                </tr>
                <tr>
                    <th>ID</th>
                    <th>Text</th>
                    <th>Project</th>
                    <th>created</th>
                    <th>User</th>
                    <th>updated</th>
                    <th>Status</th>
                    <th></th>

                </tr>
                </thead>
                <tbody>
                {todos.map((todo) => <ToDoItem key={todo.id}
                                               todo={todo}
                                               todoDelete={todoDelete}/>)}
                </tbody>
            </table>
            <Link to="/todos/create/"> New TODO </Link>
        </div>
    );
};

export default ToDosList;
