# SimpleMMO Guild Level Calculator
## Overview

This Python script calculates the average level of players in a SimpleMMO guild. It makes use of the SimpleMMO API to retrieve player data from the guild and then computes the average level.

## How it works

The script sends POST requests to the SimpleMMO API endpoint for retrieving guild member data. It keeps track of the number of requests made to respect the API rate limit which is 40 requests per minute. The script is designed to be efficient and responsive, it runs continuously until all guild members' levels have been processed.

While processing, the script prints out a progress percentage and an estimated time of completion (ETA). This way, users can track the progress of the script and have an idea of when the operation will complete.

The script accepts two inputs: API key and Guild ID. These need to be replaced with your API key and Guild ID in order to work properly.

## Usage

To use this script, follow these steps:
```
    Clone or download the script.
    Replace the placeholders 'your_api_key' and 'your_guild_id' in the script with your API key and Guild ID.
    Run the script.
```
After running the script, you will see the script's progress and ETA printed on the console. Once the script finishes executing, it will print out the average level of players in the guild.

## Limitations
```
    The script is constrained by the SimpleMMO API's rate limit of 40 requests per minute.
    The script calculates the average level based on the player level data at the time of execution. It does not account for level changes that happen after it starts running.
```
