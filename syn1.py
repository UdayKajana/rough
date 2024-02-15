import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
num_rows = 1000
df = pd.DataFrame()
columns = {
"__time": np.datetime64,
'subscriber_key':int,
'cell_key':int,
'record_type':str,
'disposition_key':str,
'ue_ctx_rel_req_disp_key':str,
'manufacturer':str,
'model':str,
'attach_apn':str,
'pdncon_failure_cause_code':str,
'pdncon_apn':float,
'attach_attempt':float,
'attach_failure':float,
'attach_failure_cause_code':float,
'average_codeword0_mimo_wideband_cqi':float,
'average_ul_sinr':float,
'cmr_serving_reference_signal_received_power_rsrp_access':float,
'cmr_serving_reference_signal_received_power_rsrp_last':float,
'context_drop':float,
'context_release':float,
'daily_agg_date_key':float,
'date_key':float,
'default_bearer_dl_rlc_transmitted_volume_s1':float,
'default_bearer_dl_rlc_transmitted_volume_s2':float,
'default_bearer_dl_rlc_transmitted_volume_s3':float,
'default_bearer_dl_rlc_transmitted_volume_s4':float,
'default_bearer_dl_rlc_transmitted_volume_s5':float,
'default_bearer_dl_rlc_transmitted_volume_s6':float,
'default_bearer_dl_rlc_transmitted_volume_s7':float,
'default_bearer_dl_rlc_transmitted_volume_s8':float,
'default_bearer_dl_rlc_transmit':float,
'dl_rlc_throughput_mbps_s1':float,
'dl_rlc_throughput_mbps_s2':float,
'dl_rlc_throughput_mbps_s3':float,
'dl_rlc_throughput_mbps_s4':float,
'dl_rlc_throughput_mbps_s5':float,
'dl_rlc_throughput_mbps_s6':float,
'dl_rlc_throughput_mbps_s7':float,
'dl_rlc_throughput_mbps_s8':float,
'double_s1':float,
'enb_cfcq2':float,
'enb_uectxtrelease_distance':float,
'enb_uectxtrelease_enodeb_key':float,
'enb_uectxtrelease_tti_bundling_mode':float,
'end_time':int,
'final_ul_sinr_db':int,
'hourly_agg_date_key':int,
'imsi':int,
'init_ul_sinr_db':float,
'last_distance_miles':float,
'number_of_sgnb_requests':float,
'pdncon_attempt':float,
'pdncon_failure':float,
'qci9':float,
'record_time':int,
'rrc_conn_reestablish_enodeb_key':float,
'rrc_conn_reestablish_tti_bundling_mode':float,
'start_time':int,
'ue_mobility_eval_enodeb_key':float,
'ue_mobility_eval_serving_rsrp':float,
'ue_ms1_cqi_denominator':float,
'ue_ms1_cqi_numerator':float,
'ue_ms1_enodeb_key':float,
'ue_ms2_cqi_denominator':float,
'ue_ms2_cqi_numerator':float,
'ue_ms2_enodeb_key':float,
'ue_ms3_cqi_denominator':float,
'ue_ms3_cqi_denominator':float,
'ue_ms3_cqi_numerator':float,
'ue_ms3_enodeb_key':float,
'ue_trs1_enodeb_key':float,
'ue_trs1_kbps_dl':float,
'ue_trs2_enodeb_key':float,
'ue_trs2_kbps_dl':float,
'ue_trs3_enodeb_key':float,
'ue_trs3_kbps_dl':float,
'uemeasment_sample1_last_pusch_sinr':float,
'uemeasment_sample2_last_pusch_sinr':float,
'uemeasment_sample3_last_pusch_sinr':float,
'uetrafficrep_sample1_meastime':float,
'uetrafficrep_sample1_thp_pdcpvol_trunk_dl':float,
'uetrafficrep_sample2_meastime':float,
'uetrafficrep_sample2_thp_pdcpvol_trunk_dl':float,
'uetrafficrep_sample3_meastime':float,
'uetrafficrep_sample3_thp_pdcpvol_trunk_dl':float,
'volte_call_category_key':float
}

for col, dtype in columns.items():
    if dtype == np.datetime64:
        start_date = datetime(2020, 1, 1)
        end_date = datetime(2023, 12, 31)
        df[col] = [random.choice(pd.date_range(start=start_date, end=end_date)) for _ in range(num_rows)]
    elif dtype == int:
        df[col] = np.random.randint(0,1, size=num_rows)
    elif dtype == float:
        df[col] = np.random.randint(0,1, size=num_rows)
    elif dtype == str:
        df[col] = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 10))) for _ in range(num_rows)]t
print(df.head())
