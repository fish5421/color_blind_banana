from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
from pathlib import Path



# Import fast.ai Library
# from fastai import *
# from fastai.vision import *

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
application = Flask(__name__)

# Model saved with Keras model.save()


# path = Path("path")
# classes = ['jaguar_s-type', 'mitsubishi_3000gt', 'mitsubishi_mirage', 'saturn_ion', 'mercedes benz_c320', 'mitsubishi_galant', 'saturn_sl2', 'dodge_nitro', 'chevrolet_lumina', 'mazda_rx8', 'chevrolet_suburban', 'volkswagen_newbeetle', 'jeep_wrangler', 'suzuki_xl7', 'honda_ridgeline', 'honda_fit', 'lincoln_mkx', 'bmw_530i', 'jeep_commander', 'mazda_6', 'toyota_rav4', 'mercedes benz_c230', 'toyota_avalon', 'toyota_celica', 'kia_soul', 'ford_windstar', 'infiniti_g37', 'nissan_versa', 'jeep_cherokee', 'chrysler_town&country', 'pontiac_sunfire', 'mitsubishi_eclipse', 'scion_xb', 'bmw_328i', 'ford_edge', 'subaru_impreza', 'ford_excursion', 'kia_forte', 'lincoln_towncar', 'mercury_villager', 'infiniti_i30', 'hyundai_azera', 'honda_prelude', 'volvo_s40', 'jeep_grand', 'oldsmobile_intrigue', 'toyota_solara', 'scion_xa', 'bmw_535i', 'honda_s2000', 'audi_tt', 'oldsmobile_silhouette', 'gmc_jimmy', 'ford_mustang', 'mercedes benz_e320', 'mercedes benz_ml350', 'infiniti_qx4', 'buick_regal', 'mercedes benz_c240', 'honda_passport', 'hummer_h3', 'porsche_cayenne', 'mercedes benz_s550', 'cadillac_catera', 'volvo_c70', 'bmw_528i', 'ford_focus', 'buick_lacrosse', 'mercedes benz_c300', 'ford_e350', 'honda_delsol', 'acura_rdx', 'ford_f150', 'fiat_five hundred', 'chevrolet_caprice', 'lincoln_mkz', 'acura_tl', 'chevrolet_camaro', 'dodge_journey', 'honda_odyssey', 'dodge_avenger', 'kia_sportage', 'saturn_vue', 'hyundai_tucson', 'volvo_xc90', 'nissan_sentra', 'buick_enclave', 'bmw_z4', 'mercedes benz_c280', 'pontiac_montana', 'mercedes benz_sl500', 'gmc_terrain', 'jeep_cj7', 'jeep_compass', 'saturn_aura', 'gmc_envoy', 'toyota_camry', 'bmw_540i', 'bmw_745i', 'subaru_forester', 'lexus_is250', 'plymouth_neon', 'chrysler_pacifica', 'toyota_mr2', 'gmc_suburban', 'ford_e250', 'acura_rsx', 'mitsubishi_lancer', 'hyundai_genesis', 'mazda_5', 'chevrolet_s10', 'nissan_pathfinder', 'mercury_grandmarquis', 'chevrolet_c-k1500', 'lexus_ls400', 'oldsmobile_aurora', 'bmw_m3', 'dodge_magnum', 'buick_parkavenue', 'nissan_altima', 'toyota_yaris', 'lincoln_ls', 'ford_f250', 'cadillac_seville', 'kia_sedona', 'ford_f450', 'mazda_3', 'ford_thunderbird', 'jaguar_xj', 'chrysler_voyager', 'lexus_es330', 'dodge_challenger', 'chevrolet_cobalt', 'volvo_s80', 'dodge_dart', 'mercury_mariner', 'chevrolet_venture', 'bmw_330ci', 'toyota_supra', 'isuzu_trooper', 'toyota_4runner', 'gmc_sonoma', 'chevrolet_avalanche', 'lexus_is350', 'porsche_boxster', 'lincoln_aviator', 'buick_century', 'mercedes benz_e350', 'acura_integra', 'volkswagen_jetta', 'audi_a4', 'gmc_canyon', 'nissan_titan', 'honda_accord', 'chevrolet_malibu', 'landrover_discovery', 'lexus_gs300', 'chevrolet_tracker', 'bmw_m5', 'chrysler_concorde', 'mercury_sable', 'bmw_335i', 'infiniti_g35', 'nissan_xterra', 'lexus_sc430', 'mercedes benz_e500', 'cadillac_escalade', 'chevrolet_hhr', 'cadillac_cts', 'kia_rio', 'volkswagen_gti', 'nissan_armada', 'nissan_350z', 'toyota_tacoma', 'pontiac_bonneville', 'dodge_durango', 'lexus_es350', 'acura_legend', 'bmw_x5', 'mazda_rx7', 'pontiac_grandprix', 'subaru_outback', 'pontiac_firebird', 'mercury_milan', 'ford_fiesta', 'chevrolet_tahoe', 'mazda_protege', 'volkswagen_touareg', 'volvo_s70', 'bmw_323i', 'mercury_mountaineer', 'audi_a8', 'bmw_325i', 'hyundai_elantra', 'lincoln_mark', 'volvo_v70', 'infiniti_m35', 'lincoln_navigator', 'jaguar_x-type', 'oldsmobile_cutlass', 'bmw_740i', 'lincoln_continental', 'chevrolet_chevelle', 'nissan_300zx', 'toyota_prius', 'buick_lucerne', 'dodge_caliber', 'nissan_quest', 'pontiac_gto', 'pontiac_g6', 'chevrolet_c10', 'ford_taurus', 'pontiac_vibe', 'hyundai_tiburon', 'lexus_is300', 'chevrolet_aveo', 'jeep_liberty', 'porsche_911', 'chrysler_crossfire', 'subaru_wrx', 'jeep_cj5', 'chevrolet_uplander', 'cadillac_eldorado', 'ford_ranger', 'chevrolet_express', 'honda_civic', 'nissan_murano', 'chrysler_sebring', 'suzuki_sx4', 'toyota_tercel', 'saturn_l300', 'mitsubishi_endeavor', 'honda_pilot', 'pontiac_torrent', 'toyota_t100', 'volkswagen_bug', 'mercedes benz_s430', 'chevrolet_corvette', 'volkswagen_golf', 'ford_contour', 'infiniti_i35', 'toyota_landcruiser', 'ford_fusion', 'saturn_l200', 'mazda_626', 'chevrolet_montecarlo', 'dodge_grand caravan', 'kia_sephia', 'ford_escort', 'plymouth_voyager', 'ford_escape', 'toyota_sienna', 'bmw_545i', 'toyota_matrix', 'mercedes benz_ml320', 'hyundai_accent', 'bmw_x3', 'nissan_frontier', 'pontiac_grandam', 'nissan_rogue', 'volkswagen_cc', 'subaru_legacy', 'acura_rl', 'saab_9-5', 'chevrolet_astro', 'dodge_neon', 'mitsubishi_outlander', 'audi_s4', 'mazda_millenia', 'buick_lesabre', 'volkswagen_passat', 'dodge_intrepid', 'jeep_patriot', 'chevrolet_sonic', 'dodge_stratus', 'lexus_rx330', 'buick_rendezvous', 'cadillac_srx', 'hyundai_santafe', 'buick_riviera', 'volvo_s60', 'acura_tsx', 'volkswagen_eos', 'mercury_cougar', 'bmw_750i', 'hyundai_sonata', 'acura_cl', 'chevrolet_impala', 'ram_1500', 'ford_expedition', 'landrover_rangerover', 'chevrolet_bel air', 'oldsmobile_bravada', 'toyota_echo', 'mazda_mpv', 'gmc_acadia', 'ford_e150', 'ford_freestar', 'bmw_525i', 'oldsmobile_alero', 'audi_a3', 'mini_cooper', 'kia_spectra', 'bmw_z3', 'saturn_sl1', 'gmc_sierra', 'pontiac_transam', 'chevrolet_traverse', 'lexus_ls430', 'gmc_yukon', 'toyota_highlander', 'nissan_maxima', 'kia_sorento', 'dodge_dakota', 'hummer_h2', 'kia_amanti', 'suzuki_forenza', 'scion_tc', 'chevrolet_el camino', 'audi_a6', 'toyota_sequoia', 'toyota_pickup', 'volvo_xc70', 'mercedes benz_clk320', 'bmw_550i', 'mitsubishi_montero', 'infiniti_q45', 'saab_9-3', 'cadillac_deville', 'toyota_tundra', 'chevrolet_blazer', 'nissan_240sx', 'chrysler_200', 'chevrolet_colorado', 'lexus_es300', 'ford_crown victoria', 'ford_bronco', 'honda_cr-v', 'mercedes benz_ml500', 'mazda_tribute', 'ford_f350', 'infiniti_fx35', 'dodge_ram', 'volvo_850', 'cadillac_sts', 'ford_f100', 'toyota_corolla', 'volkswagen_beetle', 'acura_mdx', 'chevrolet_nova', 'kia_optima', 'mazda_mx5', 'chevrolet_silverado', 'scion_xd', 'ford_explorer', 'dodge_charger', 'chevrolet_cruze', 'infiniti_qx56', 'chrysler_300', 'mercedes benz_s500', 'chevrolet_equinox', 'toyota_fjcruiser', 'lexus_rx300', 'smart_fortwo', 'volkswagen_rabbit', 'bmw_330i', 'ford_five hundred', 'chrysler_pt cruiser', 'pontiac_g5', 'honda_element', 'isuzu_rodeo', 'lexus_gx470', 'chevrolet_prizm', 'chevrolet_trailblazer', 'chevrolet_cavalier']
# data2 = ImageDataBunch.single_from_classes(path, classes, tfms=get_transforms(max_lighting=0.2, max_zoom=1.5, max_warp=0.2), size=224).normalize(imagenet_stats)
# learn = create_cnn(data2, models.resnet34)
# learn.load('stage-2')




def model_predict(img_path):
    """
       model_predict will return the preprocessed image
    """

    img = open_image(img_path)
    pred_class,pred_idx,outputs = learn.predict(img)
    return pred_class





@application.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@application.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path)
        return preds
    return None


if __name__ == '__main__':

    application.run()
