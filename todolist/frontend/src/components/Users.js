import React from 'react';

const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.id}</td>
            <td>{user.username}</td>
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
            <tr><th>USERS</th></tr>
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
