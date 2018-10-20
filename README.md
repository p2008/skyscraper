# skyscraper_workshop

## Models

### room
* id - primary key
* name 
* capacity
* projector_is_available

### reservation
* id - primary key
* date
* room_id - foreign key
* comment

## User stories 

As a user, I want to see all rooms.
As a user, I want to see rooms with their status that is free or busy.
As a user, I want to see rooms with links to edit or remove.
As a user, I want to edit room on click edit.
As a user, I want to remove room on click remove.
As a user, I want to see room details when click on name room.
As a user, I want to see room details with name, capacity and projector avalibility.
As a user, I want to see room details with list of days when room is busy.
As a user, I want to see room details with only overlapping list of days.
As a user, I want to see room details with link to reservation.
As a user, I want to add new room.
As a user, I want to input name, capacity, project avalibility on editing room.
As a user, I want to see reservation details with only overlapping list of days.
As a user, I want to input date on reservation room.
