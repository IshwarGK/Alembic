It is Short Overview about Alembic.

What is Alembic and Why we need Alembic?

Almbic is a tool which can be used for the creation and migration of relational database. Alembic uses SQLAlchemy as underlying engine for development. Alembic is used as database migration tool.


For installation use following link.
https://alembic.zzzcomputing.com/en/latest/front.html

For the Tutorial regarding Alembic use following link,
https://alembic.zzzcomputing.com/en/latest/tutorial.html

Points
1. You write the table defination for Alembic.(upgrade scripts)
2. Also, downgrate script if we want to downgrate.
3. Firstly, you need to create the revision with proper message. Message is required to understand reson of creating the revision.
4. In the create file you can write the scripts.
5. Run the following command to upgrate,
alembic upgrade head  // head is the final point of your alembic version

also if you want to move from perticular version to only 2 version then use,
alembic upgrade +2

else, if you want to upgrate to perticular version with name then,

alembic upgrade version_name

6. To downgrate use following commands,
alembic downgrade base // base is the lowest point of your alembic version.

alembic downgrate -2

alembic downgrate version_name





