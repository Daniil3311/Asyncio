import asyncio
import datetime
import aiohttp
from more_itertools import chunked
from sqlalchemy import MetaData

from models import engine, Session, Base, SwapiPeople
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import insert

metadata = MetaData()


async def get_people(people_id):
    session = aiohttp.ClientSession()
    response = await session.get(f"https://swapi.dev/api/people/{people_id}")
    json_data = await response.json()
    await session.close()
    return json_data


async def paste_to_db(persons_json):
    async with Session() as session:
        #orm_objects = [SwapiPeople(json=item) for item in persons_json]

        session.add_all([
            SwapiPeople(name='daniil')
        ])
        await session.commit()


async def main():
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)

    person_coros = (get_people(i) for i in range(1, 2))
    person_coros_chunked = chunked(person_coros, 5)
    tasks = []
    for person_coros_chunk in person_coros_chunked:
        persons = await asyncio.gather(*person_coros_chunk)
        tasks.append(asyncio.create_task(paste_to_db(persons)))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = datetime.datetime.now()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())


    print(datetime.datetime.now() - start)




