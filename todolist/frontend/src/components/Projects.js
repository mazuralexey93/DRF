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
            <tr>
                <th>ID</th>
                <th>Title</th>
                <th>Link</th>
                <th>Users</th>

            </tr>
            {projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    );
};

export default ProjectsList;
