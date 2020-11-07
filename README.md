# Egyptian national ID validator and data-extractor API

[![Actions Status](https://github.com/waleedhammam/national_id/workflows/national_id/badge.svg?query=branch%3Amain)](https://github.com/waleedhammam/national_id/actions?query=branch%3Amain)
[![codecov.io](https://codecov.io/github/waleedhammam/national_id/coverage.svg?branch=main)](https://codecov.io/github/waleedhammam/national_id?branch=main)

## Requirments

- python3.6 or later
- pip3
- bottle

## How to run

- Install requirments `pip3 install -r requirements.txt`
- Run `python3 server.py`
- Server will be running on port 8001
- Endpoint can be reached at http://localhost:8001/get_info

## Endpoint

- `/get_info`
  - Accepts post requests with "Content-Type: application/json" Header
    - Example request:

      ```bash
      curl -H "Content-Type: application/json" -d '{"id_number": "29009121201812"}' -XPOST http://localhost:8001/get_info
      ```

  - Response
    - 200 OK, json_info: national id is validated and info extraction ok
    - 400 Bad Request: Wrong national id number
    - 500 Internal Server Error: Invalid request from user (invalid json, invalid form of data)

    Example response:

      ```bash
      {"nationl_id_data": {"year_of_birth": "1994", "month_of_birth": "9", "day_of_birth": "15", "governorate": "Al Daqhlia", "type": "Male"}}
      ```

## Validations and checks

- According to [this source](https://ar.wikipedia.org/wiki/%D8%A8%D8%B7%D8%A7%D9%82%D8%A9_%D8%A7%D9%84%D8%B1%D9%82%D9%85_%D8%A7%D9%84%D9%82%D9%88%D9%85%D9%8A_%D8%A7%D9%84%D9%85%D8%B5%D8%B1%D9%8A%D8%A9)

The national ID consists of the following:

  ```bash
  +-+--+--+--+--+----+-+
  |2|90|01|01|12|3456|7|
  +--------------------+
  |A|B |C |D |E | F  |G|
  +-+--+--+--+--+----+-+
  ```

- A -> The century: A=2 From (1900-1999), A=3 From (2000-2099)
- B~D (Date of birth):
    B -> Year of birth
    C -> Month of birth
    D -> Day of birth
- E -> Governorate code ex: {12: "Al Daqhlia"}
- F -> Unique code. (Odd is male, Even is female)
- G -> Check digit for verification

## How to run tests

- Lib test: `pytest -s tests/test_national_id.py`
- Test the endpoint `python3 -m pytest -s tests/test_endpoint.py`

## Dockerfile

- You can build and run the dockerfile in `docker directory`
  `docker build -t waleedhammam/national_id .`
