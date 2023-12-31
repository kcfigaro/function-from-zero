curl -X 'POST' \
  'http://127.0.0.1:8000/scrape/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "amazon",
  "length": 2
}'

echo ""
