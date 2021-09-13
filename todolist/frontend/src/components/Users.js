import React from 'react';
import {Link} from "react-router-dom";

const UserItem = ({user}) => {
    return (
        <tr>
            <td><Link to={`/user/${user.id}/`}>{user.id}</Link></td>
            <td><Link to={`/user/${user.username}/`}>{user.username}</Link></td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
        </tr>
    );
};

const UsersList = ({users}) => {
    return (
        <table className='table'>
            <thead>
            <tr>
                <th>ID</th>
                <th>Username</th>
                <th>Firstname</th>
                <th>Lastname</th>
                <th>Email</th>
            </tr>
            </thead>
            <tbody>
            {users.map((user) => <UserItem  key={user.id} user={user}/>)}
            </tbody>
        </table>
    );
};

export default UsersList;