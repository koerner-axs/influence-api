client = InfluenceClient(client_id='', client_secret='')


# Trying to retrieve the JWT token from endpoints https://api-prerelease.influenceth.io/v1/auth/token and https://api.influenceth.io/v1/auth/tokenwith method: "POST", body: JSON.stringify({
#         grant_type: "client_credentials",
#         client_id: process.env.CLIENT_ID,
#         client_secret: process.env.CLIENT_SECRET,
#       }), got { error: 'unsupported_grant_type' }. Any idea what I am doing wrong?
