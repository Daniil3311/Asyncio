import asyncio
import datetime
import aiohttp
from more_itertools import chunked
from sqlalchemy import MetaData
from models import engine, Session, Base, Swapipeople
#import requests


metadata = MetaData()


async def get_people(people_id):
    session = aiohttp.ClientSession()
    response = await session.get(f"https://swapi.dev/api/people/{people_id}")
    json_data = await response.json()
    await session.close()
    return json_data


async def paste_to_db(persons_json):
    async with Session() as session:
        orm_objects = [Swapipeople(
                                    name=item['name'],
                                    films=','.join(item['films']),
                                    eye_color=item['eye_color'],
                                    birth_year=item['birth_year'],
                                    species=','.join(item['species']),
                                    skin_color=item['skin_color'],
                                    mass=item['mass'],
                                    homeworld=','.join(item['homeworld']),
                                    height=item['height'],
                                    hair_color=item['hair_color'],
                                    gender=item['gender'],
                                    starships=','.join(item['starships']),
                                    vehicles=','.join(item['vehicles']),
                                    ) for item in persons_json]
        session.add_all(orm_objects)
        await session.commit()
        #print(persons_json)

async def main():
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)

    person_coros = (get_people(i) for i in range(20, 70))
    person_coros_chunked = chunked(person_coros, 10)

    for person_coros_chunk in person_coros_chunked:
        persons = await asyncio.gather(*person_coros_chunk)
        asyncio.create_task(paste_to_db(persons))
    tasks = asyncio.all_tasks() - {asyncio.current_task(), }
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = datetime.datetime.now()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

    print(datetime.datetime.now() - start)



