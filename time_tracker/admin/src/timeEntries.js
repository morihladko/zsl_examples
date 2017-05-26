import React from 'react';
import { List, Edit, Datagrid, EmailField, TextField, DisabledInput, TextInput,
    LongTextInput, EditButton, SimpleForm, Create, Filter, DateField,
    ReferenceField, ReferenceInput, SelectInput } from 'admin-on-rest/lib/mui';

export const TimeEntryFilter = (props) => (
    <Filter {...props}>
        <ReferenceInput label="User" source="user_id" reference="users">
            <SelectInput optionText="fullname" />
        </ReferenceInput>
        <TextInput label="Search" source="what_like"/>
    </Filter>
);

export const TimeEntryList = (props) => (
    <List title="All time entries" {...props} filters={<TimeEntryFilter/>}>
        <Datagrid>
            <TextField source="id" />
            <ReferenceField label="User" source="user_id" reference="users">
                <TextField source="fullname" />
            </ReferenceField>
            <DateField source="start_time" showTime />
            <DateField source="end_time" showTime />
            <TextField source="what" />
            <EditButton/>
        </Datagrid>
    </List>
);

export const TimeEntryEdit = (props) => (
    <Edit title="Time entry" {...props}>
        <SimpleForm>
            <DisabledInput source="id"/>
            <ReferenceField label="User" source="user_id" reference="users">
                <TextField source="fullname" />
            </ReferenceField>
            <DateField source="start_time" showTime />
            <DateField source="end_time" showTime />
            <LongTextInput source="what" />
        </SimpleForm>
    </Edit>
);
