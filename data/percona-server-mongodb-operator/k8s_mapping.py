from acto.input.known_schemas import *

WHITEBOX = [
    K8sField(['spec', 'backup', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'backup', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'backup', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'backup', 'image'], ImageSchema),
    K8sField(['spec', 'backup', 'runtimeClassName'], K8sStringSchema),
    K8sField(['spec', 'backup', 'serviceAccountName'], ServiceAccountNameSchema),
    K8sField(['spec', 'backup', 'tasks', 'ITEM', 'schedule'], CronJobScheduleSchema),
    K8sField(['spec', 'image'], ImageSchema),
    K8sField(['spec', 'imagePullPolicy'], ImagePullPolicySchema),
    K8sField(['spec', 'replsets', 'ITEM', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'nodeSelector'], NodeSelectorSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'podDisruptionBudget'], PodDisruptionBudgetSpecSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'priorityClassName'], PriorityClassNameSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'volumeSpec', 'persistentVolumeClaim', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'volumeSpec', 'persistentVolumeClaim', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'volumeSpec', 'persistentVolumeClaim', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'volumeSpec', 'persistentVolumeClaim', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'mongos', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'sharding', 'mongos', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'sharding', 'mongos', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'sharding', 'mongos', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'mongos', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'mongos', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'sharding', 'mongos', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'sharding', 'mongos', 'tolerations'], TolerationsSchema),
]

BLACKBOX = [
    K8sField(['spec', 'backup', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'backup', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'backup', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'volumeSpec', 'persistentVolumeClaim', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'replsets', 'ITEM', 'volumeSpec', 'persistentVolumeClaim', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'volumeSpec', 'persistentVolumeClaim', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'sharding', 'configsvrReplSet', 'volumeSpec', 'persistentVolumeClaim', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'mongos', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'sharding', 'mongos', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'sharding', 'mongos', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'sharding', 'mongos', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'mongos', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'sharding', 'mongos', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'sharding', 'mongos', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'sharding', 'mongos', 'tolerations'], TolerationsSchema),
]