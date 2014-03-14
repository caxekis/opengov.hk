# Server Environment Setup

1. Add settings for `your_env` to the `fabfile.py`
1. `fab your_env push_key`
1. `fab your_env generate_deploy_key `
	1. Add `id_rsa.pub` to Github repo as deploy key  
1. `fab your_env setup`
