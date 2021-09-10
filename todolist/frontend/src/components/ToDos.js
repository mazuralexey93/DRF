import React from 'react';

const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.text}</td>
            <td>{todo.user}</td>
            <td>{todo.project}</td>
            <td>{todo.is_active}</td>
        </tr>
    );
};

const ToDosList = ({todos}) => {
    return (
        <table className='table'>
            <tr>
                <th>ID</th>
                <th>Text</th>
                <th>Project</th>
                <th>User</th>
                <th>Is_active</th>

            </tr>
            {todos.map((todo) => <ToDoItem todo={todo}/>)}
        </table>
    );
};

export default ToDosList;
