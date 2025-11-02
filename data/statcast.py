import pandas as pd
import os
from pybaseball import statcast

for x in range(2015,2026):
   start = f"{x}-01-01"
   end = f"{x}-12-31"
   csv = f"statcast_{x}.csv"
   df = statcast(start, end)
   print(f"Year {x} pulled successfully.")
   df.to_csv(csv, index=False)
   print(f"Year {x} saved successfully.")

statcast_2015 = pd.read_csv('statcast_2015.csv')
statcast_2016 = pd.read_csv('statcast_2016.csv')
statcast_2017 = pd.read_csv('statcast_2017.csv')
statcast_2018 = pd.read_csv('statcast_2018.csv')
statcast_2019 = pd.read_csv('statcast_2019.csv')
statcast_2020 = pd.read_csv('statcast_2020.csv')
statcast_2021 = pd.read_csv('statcast_2021.csv')
statcast_2022 = pd.read_csv('statcast_2022.csv')
statcast_2023 = pd.read_csv('statcast_2023.csv')
statcast_2024 = pd.read_csv('statcast_2024.csv')
statcast_2025 = pd.read_csv('statcast_2025.csv')

statcast_full = pd.concat([statcast_2015, statcast_2016, statcast_2017, statcast_2018, 
                           statcast_2019, statcast_2020, statcast_2021, statcast_2022, 
                           statcast_2023, statcast_2024, statcast_2025], ignore_index=True)

statcast_red = statcast_full.drop(['pitch_type', 'spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                                   'break_length_deprecated', 'zone', 'type', 'bb_type', 
                                   'pfx_x', 'on_3b', 'on_2b', 'on_1b', 
                                   'tfs_deprecated', 'tfs_zulu_deprecated', 'umpire', 'sv_id', 
                                   'vx0', 'vy0', 'vz0', 'ax', 
                                   'ay', 'sz_top', 'sz_bot', 'effective_speed', 
                                   'fielder_2', 'fielder_3', 'fielder_4', 'fielder_5', 
                                   'fielder_6', 'fielder_7', 'fielder_8', 'fielder_9', 
                                   'release_pos_y', 'estimated_ba_using_speedangle', 'woba_denom', 
                                   'home_score', 'away_score', 'post_away_score', 'post_home_score', 
                                   'post_fld_score', 'spin_axis', 'delta_home_win_exp', 'delta_run_exp', 
                                   'bat_speed', 'swing_length', 'estimated_slg_using_speedangle', 'delta_pitcher_run_exp', 
                                   'hyper_speed', 'home_score_diff', 'bat_score_diff', 'home_win_exp', 
                                   'bat_win_exp', 'age_pit_legacy', 'age_bat_legacy', 'n_thruorder_pitcher', 
                                   'n_priorpa_thisgame_player_at_bat', 'pitcher_days_since_prev_game', 'batter_days_since_prev_game', 'pitcher_days_until_next_game', 
                                   'batter_days_until_next_game', 'api_break_x_batter_in', 'arm_angle', 'attack_angle', 
                                   'attack_direction', 'swing_path_tilt', 'intercept_ball_minus_batter_pos_x_inches', 'intercept_ball_minus_batter_pos_y_inches',
                                   'release_pos_x', 'release_pos_z', 'hit_location', 'az', 
                                   'release_extension', 'pitch_number'], axis=1)
statcast_red = statcast_red[statcast_red.game_type == 'R']
statcast_red.to_csv('statcast_red', index=False)

statcast_years = ['statcast_2015.csv', 'statcast_2016.csv', 'statcast_2017.csv', 'statcast_2018.csv', 
                  'statcast_2019.csv', 'statcast_2020.csv', 'statcast_2021.csv', 'statcast_2022.csv', 
                  'statcast_2023.csv', 'statcast_2024.csv', 'statcast_2025.csv']

for file in statcast_years:
   if os.path.exists(file):
      os.remove(file)
      print(f"File '{file}' deleted successfully.")
   else:
      print(f"File '{file}' does not exist.")