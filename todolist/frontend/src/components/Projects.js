import React from 'react';
import {Link} from "react-router-dom";
import searchTextChange from '../App.js'
import findProjects from '../App.js'


const ProjectItem = ({project, projectDelete}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td><Link to={`/projects/${project.id}/`}>{project.name}</Link></td>
            <td>{project.link}</td>
            <td>{project.users}</td>
            <td>
                <button onClick={() => projectDelete(project.id)}>
                    Delete
                </button>
            </td>
        </tr>
    );
};

const ProjectsList = ({projects, projectDelete}) => {
    return (
       <form>
            <div className="projects-list">
            {/*<input type="text" placeholder="Search..."*/}
            {/*           onChange={(event) =>*/}
            {/*               new searchTextChange(event.target.value)} />*/}
            {/*    <button onClick={findProjects}>Search</button>*/}


            <table className='table'>
                <thead>
                <tr>
                    <th>PROJECTS</th>
                </tr>
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Link</th>
                    <th>Users</th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {projects.map((project) => <ProjectItem key={project.id}
                                                        project={project}
                                                        projectDelete={projectDelete}/>)}
                </tbody>
            </table>
            <Link to="/projects/create/"> New Project </Link>
        </div>
       </form>
    )
};

export default ProjectsList;
