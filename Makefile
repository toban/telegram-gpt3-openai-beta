-include .env


docker:
	echo 
	docker build --build-arg=CHAT_ID="${CHAT_ID}" \
		--build-arg=BOT_NAME=${BOT_NAME} \
		--build-arg=BOT_TOKEN=${BOT_TOKEN} \
		--build-arg=VOICE_PITCH=${VOICE_PITCH} \
		--build-arg=API_KEY="${API_KEY}" \
		. < Dockerfile --no-cache
