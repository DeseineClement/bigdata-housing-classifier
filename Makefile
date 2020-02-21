DATASET_REQUIREMENT_FILE	= bigdata-housing-classifier-dataset/requirements.txt
DATASET_VIRTUALENV			= dataset-venv
DATASET_ACTIVATE_SCRIPT		= $(DATASET_VIRTUALENV)/bin/activate
DATASET_ENTRY_POINT_FILE	= bigdata-housing-classifier-dataset/src/dataset.py

DATASET_OUTPUT_DIRECTORY	= dataset
DATASET_OUTPUT_FILE			= $(DATASET_OUTPUT_DIRECTORY)/data.csv
DATASET_OUTPUT_FILE_ROWS	= 10000

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

# $(1): path to the dataset output directory
# $(3): path to the dataset output file
# $(3): path to the virtualenv activate script file
# $(4): path to the dataset entry point file
# $(5): number of rows of the dataset output file
define generate_dataset
	@if [ ! -d $(1) ]; then	\
		mkdir -p $(1);		\
	fi
	@(source $(3) && python $(4) --output-file=$(2) --rows=$(5))
endef

virtualenv: virtualenv.dataset virtualenv.classifier

virtualenv.dataset:
	$(call generate_virtualenv,$(DATASET_VIRTUALENV))
	$(call install_dependencies,$(DATASET_ACTIVATE_SCRIPT),$(DATASET_REQUIREMENT_FILE))

virtualenv.classifier:
	$(call generate_virtualenv,$(CLASSIFIER_VIRTUALENV))
	$(call install_dependencies,$(CLASSIFIER_ACTIVATE_SCRIPT),$(CLASSIFIER_REQUIREMENT_FILE))

dataset: virtualenv.dataset
	$(call generate_dataset,$(DATASET_OUTPUT_DIRECTORY),$(DATASET_OUTPUT_FILE),$(DATASET_ACTIVATE_SCRIPT),$(DATASET_ENTRY_POINT_FILE),$(DATASET_OUTPUT_FILE_ROWS))

.PHONY: virtualenv virtualenv.dataset virtualenv.classifier dataset