PASSWORD_FILE := vault-password.txt
SECRETS_BUCKET := "tnris-secrets"
APP_NAME := lake-gallery


FORCE:

.vault/.push/%: FORCE
	mkdir -p $(dir $@)
	cp $(notdir $@) $@
	ansible-vault encrypt --vault-password-file $(PASSWORD_FILE) $@
	aws s3 cp $@ s3://$(SECRETS_BUCKET)/$(APP_NAME)/.vault/$(notdir $@)

push-secrets: \
	.vault/.push/set_env.sh

.vault/.pull/%: FORCE
	mkdir -p $(dir $@)
	aws s3 cp s3://$(SECRETS_BUCKET)/$(APP_NAME)/.vault/$(notdir $@) $@

secrets/%: .vault/.pull/%
	ansible-vault decrypt --vault-password-file $(PASSWORD_FILE) $<
	mv $< ./$(notdir $@)

pull-secrets: \
	secrets/set_env.sh
