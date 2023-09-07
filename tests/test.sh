#!/bin/bash

echo "Get family members for user ID 1:"
curl "http://127.0.0.1:5000/family_members?id=1"

echo "Get family members for user ID 1488258600:"
curl "http://127.0.0.1:5000/family_members?id=1488258600"

echo "Get temperature for user ID 1488258600:"
curl "http://127.0.0.1:5000/temperature?id=1488258600"

echo "Get sleep stages for user ID 1488258600:"
curl "http://127.0.0.1:5000/sleep_stages?id=1488258600"

echo "Get sleep score for user ID 1488258600:"
curl "http://127.0.0.1:5000/sleep_score?id=1488258600"
