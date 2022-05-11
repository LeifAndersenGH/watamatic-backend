import os
from core import api


if (__name__ == '__main__'):
    PORT=os.enviorn.get('PORT')
    api.run(debug=True, port=PORT, host='0.0.0.0')
