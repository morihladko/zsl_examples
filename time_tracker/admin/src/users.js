import React from 'react';
import { List, Edit, Datagrid, EmailField, TextField, DisabledInput, TextInput,
    EditButton, SimpleForm, Create, Filter } from 'admin-on-rest/lib/mui';

function PostFilter(props) {
    return (
        <Filter {...props}>
            <TextInput label="Search" source="q" alwaysOn />
        </Filter>
    );
}

export function UserList(props) {
    return (
        <List title="All users" {...props} filters={<PostFilter/>}>
            <Datagrid>
                <TextField source="id" />
                <TextField source="fullname" />
                <TextField source="username" />
                <EmailField source="email" />
                <EditButton/>
            </Datagrid>
        </List>
    );
}

export function UserName({user}) {
    let name = user ? user.fullname : '';

    return (
        <span>User {name}</span>
    )
}

export function UserEdit(props) {
    return (
        <Edit title={<UserName />} {...props}>
            <SimpleForm>
                <DisabledInput source="id"/>
                <DisabledInput source="username"/>
                <TextInput source="fullname"/>
                <TextInput source="email" type="email"/>
            </SimpleForm>
        </Edit>
    );
}

export function UserCreate(props) {
    return (
        <Create {...props}>
            <SimpleForm>
                <TextInput source="username"/>
                <TextInput source="fullname"/>
                <TextInput source="email" type="email"/>
            </SimpleForm>
        </Create>
    );
}