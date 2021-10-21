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

// const ProjectInstance = ({projects}) => {
//     let {id} = useParams()
//     let filteredProjects = projects.filter((project) => project.id === +id)
//     return (
//         <table className='table'>
//             <thead>
//             <tr><th>PROJECT DETAILS</th></tr>
//             <tr>
//                 <th>ID</th>
//                 <th>Title</th>
//                 <th>Link</th>
//                 <th>Users</th>
//             </tr>
//             </thead>
//             <tbody>
//             {filteredProjects.map((project) => <ProjectItem key={project.id} project={project}/>)}
//             </tbody>
//         </table>
//     );
// };

const ProjectInstance = ({getProject, project}) => {

    let {id} = useParams();
    console.log(id, project)
    if (!Object.keys(project).length || project.id !== +id) {
        getProject(id)
    }
    let users = project.users ? project.users : [];
    return (
        <div>
            <h2>{project.name}</h2>
            Link: <a href={project.link}>{project.link}</a>
            <p></p>
            Users:
            <ol>
                {users.map((user) => <ProjectItem key={user.id} project={user}/>)}
                {project.users}
            </ol>
        </div>
    )
}

export default ProjectInstance;
