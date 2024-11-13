from db import Session, Race


def add_race(gp, laps):
    with Session() as session:
        race = Race(gp=gp, laps=laps)
        session.add(race)
        session.commit()
        session.refresh(race)
        return race.id


def get_races():
    with Session() as session:
        return session.query(Race).all()


def get_race(id):
    with Session() as session:
        return session.query(Race).where(Race.id == id).first()


def update_race(id, gp, laps):
    with Session() as session:
        race = session.query(Race).filter_by(id=id).first()
        race.gp = gp
        race.laps = laps
        session.commit()
        return "Дані оновлено"


def delete_race(id):
    with Session() as session:
        race = session.query(Race).filter_by(id=id).first()
        session.delete(race)
        session.commit()
        return "Гонка видалена"