from sdg.open_sdg import open_sdg_build

def alter_meta(meta):
    # Drop an reporting_status field in the metadata.
    del meta['reporting_status']
    return meta

open_sdg_build(config='config_data.yml', alter_meta=alter_meta)
