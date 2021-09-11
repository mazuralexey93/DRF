import React from 'react';

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.link}</td>
            <td>{project.users}</td>
        </tr>
    );
};

const ProjectsList = ({projects}) => {
    return (
        <table className='table'>
            <thead>
            <tr>
                <th>ID</th>
                <th>Title</th>
                <th>Link</th>
                <th>Users</th>
            </tr>
            </thead>
            <tbody>
            {projects.map((project) => <ProjectItem key={project.id} project={project}/>)}
            </tbody>
        </table>
    );
};

export default ProjectsList;
