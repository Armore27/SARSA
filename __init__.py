from gym.envs.registration import register

register(
    id='Mirror-v0',
    entry_point='gym_mirror.envs:MirrorEnv'
)