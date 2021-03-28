import utils
import pb_utils
import settings
import mysql_utils


# create a logger
logger = utils.get_logger()
logger.info('yify-bay-crawler started')

# Instantiate db manager
db_manager = mysql_utils.DBManager()

# Start crawling
for i in range(151):
    logger.info('retrieving items from page {}'.format(str(i)))
    source = pb_utils.get_source_from_url(settings.YIFY_URL + ':' + str(i), logger)

    for movie in pb_utils.find_movies(source, logger):
        movie_name = db_manager.insert_movie(movie)
        logger.info('{} movie inserted'.format(movie_name))

logger.info('all items downloaded')
db_manager.close()
