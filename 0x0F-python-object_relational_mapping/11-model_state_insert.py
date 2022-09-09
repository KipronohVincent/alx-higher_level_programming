#!/usr/bin/python3
"""A script that adds object “Louisiana”
to the database hbtn_0e_6_us"""


from sys import argv


if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_st = State(name='Louisiana')
    session.add(new_st)
    new_state = session.query(State).filter(State.name == 'Louisiana').first()
    session.commit()
    print('{}'.format(new_state.id))
    session.close()
