import React from 'react';
import {useParams} from "react-router-dom";

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

const ProjectInstance = ({projects}) => {
    let {id} = useParams()
    let projectDetails = projects.filter((project) => project.id === +id)
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
            {projectDetails.map((project) => <ProjectItem key={project.id} project={project}/>)}
            </tbody>
        </table>
    );
};

export default ProjectInstance;
