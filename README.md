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

1. As a user, I want to see all rooms.
2. As a user, I want to see rooms with their status that is free or busy.
3. As a user, I want to see rooms with links to edit or remove.
4. As a user, I want to edit room on click edit.
5. As a user, I want to remove room on click remove.
6. As a user, I want to see room details when click on name room.
7. As a user, I want to see room details with name, capacity and projector availability.
8. As a user, I want to see room details with list of days when room is busy.
9. As a user, I want to see room details with only overlapping list of days.
10. As a user, I want to see room details with link to reservation.
11. As a user, I want to add new room.
12. As a user, I want to input name, capacity, project availability on editing room.
13. As a user, I want to see reservation details with only overlapping list of days.
14. As a user, I want to input date on reservation room.
15. As a user, I want to see reservations not mirrored.
16. As a user, I want to see reservations with no past date.
17. As a user, I want to search rooms.
18. As a user, I want to input name, date, capacity and projecter availability on searching rooms.
