import React from 'react';
import {Link} from "react-router-dom";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td><Link to={`/projects/${project.id}/`}>{project.name}</Link></td>
            <td>{project.link}</td>
            <td>{project.users}</td>
        </tr>
    );
};

const ProjectsList = ({projects}) => {
    return (
        <table className='table'>
            <thead>
             <tr><th>PROJECTS</th></tr>
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
