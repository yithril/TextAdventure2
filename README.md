Text adventure

Synopsis
This project is part of my assignment from "Learn Python the Hard Way."  It's a full fledged text adventure in Python, and as instructed,
I made it as complex as I could, putting in all the features I wanted.  I am using the Dungeons and Dragons 3.5 rule set as my framework.
My focus was to try to make use of design patterns to make the game modular and easy to update, so creating new areas or writing new 
characters would be easy. After I get the core system finished, then I'll focus on making a storyline.

Current Progress and Design
If you want to test out the game, simply run the Command.py file.  Rooms are json files.  The computer outputs the room description,
fills in the NPCs and Characters, as well as the items.  You can "take" and "drop" items, you can look at rooms, specific items/npcs,
or descriptions in a room.  The Wield and Wear verbs are next in line to be implemented.

The program uses a Repository for objects.  Objects are heled in a Repository cache based on a numerical id, so by simply giving the
Repository object the number "1", you get the item/npc/room/whatever you want.  The Repository is linked with the File Loader and the Factory to make
objects on demand.  I've focused on keeping each part of the game separate as possible using Model View Controller as my guideline.

Future Implementation
Combat will be the big future implementation, but I also want to finish a Character Creation screen. After Combat, the next major focus
will be on details such as NPC interaction, leveling, and feats.
