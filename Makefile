DATASET_REQUIREMENT_FILE	= bigdata-housing-classifier-dataset/requirements.txt
DATASET_VIRTUALENV			= dataset-venv
DATASET_ACTIVATE_SCRIPT		= $(DATASET_VIRTUALENV)/bin/activate

CLASSIFIER_REQUIREMENT_FILE	= requirements.txt
CLASSIFIER_VIRTUALENV		= classifier-venv
CLASSIFIER_ACTIVATE_SCRIPT	= $(CLASSIFIER_VIRTUALENV)/bin/activate

# $(1): path to the virtualenv directory
define generate_virtualenv
	@if [ ! -d $(1) ]; then		\
		virtualenv $(1);		\
	fi
endef

# $(1): path to the virtualenv activate script file
# $(2): path to the requirements.txt file
define install_dependencies
	@if [ -f $(1) ]  && [ -f $(2) ]; then		\
		(source $(1) && pip install -r $(2))	\
	fi
endef

virtualenv: virtualenv.dataset virtualenv.classifier

virtualenv.dataset:
	$(call generate_virtualenv,$(DATASET_VIRTUALENV))
	$(call install_dependencies,$(DATASET_ACTIVATE_SCRIPT),$(DATASET_REQUIREMENT_FILE))

virtualenv.classifier:
	$(call generate_virtualenv,$(CLASSIFIER_VIRTUALENV))
	$(call install_dependencies,$(CLASSIFIER_ACTIVATE_SCRIPT),$(CLASSIFIER_REQUIREMENT_FILE))

.PHONY: virtualenv virtualenv.dataset virtualenv.classifier