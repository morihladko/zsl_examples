import React, { Component } from 'react';
import { jsonServerRestClient, fetchUtils, Admin, Resource, Delete } from 'admin-on-rest';

import authClient from './authClient.js'
import { UserList, UserEdit, UserCreate } from './users'
import { TimeEntryList, TimeEntryEdit } from './timeEntries'

const httpClient = (url, options = {}) => {
    if (!options.headers) {
        options.headers = new Headers({ Accept: 'application/json' });
    }   
        
    const token = localStorage.getItem('token');
    options.headers.set('Authorization', `Bearer ${token}`);
      
    return fetchUtils.fetchJson(url, options);
}  

const App = () => (
    <Admin restClient={jsonServerRestClient('http://localhost:5000/resource', httpClient)} authClient={authClient}>
        <Resource name="users" list={UserList} edit={UserEdit} create={UserCreate} remove={Delete} />
        <Resource name="time_entries" list={TimeEntryList} edit={TimeEntryEdit} remove={Delete} />
    </Admin>
);

export default App;
