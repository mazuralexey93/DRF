import React from 'react';

const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.text}</td>
            <td>{todo.project}</td>
            <td>{todo.created_at}</td>
            <td>{todo.user}</td>
            <td>{todo.updated_at}</td>
            <td>{todo.status}</td>
        </tr>
    );
};

const ToDosList = ({todos}) => {
    return (
        <table className='table'>
            <thead>
             <tr><th>TODOS</th></tr>
            <tr>
                <th>ID</th>
                <th>Text</th>
                <th>Project</th>
                <th>created</th>
                <th>User</th>
                <th>updated</th>
                <th>Status</th>

            </tr>
            </thead>
            <tbody>
            {todos.map((todo) => <ToDoItem key={todo.id} todo={todo}/>)}
            </tbody>


        </table>
    );
};

export default ToDosList;
