from wsme import types as wtypes


class CloudkittyModule(wtypes.Base):
    """A rating extension summary

    """

    module_id = wtypes.wsattr(wtypes.text, mandatory=True)
    """Name of the extension."""

    description = wtypes.wsattr(wtypes.text, mandatory=False)
    """Short description of the extension."""

    enabled = wtypes.wsattr(bool)
    """Extension status."""

    hot_config = wtypes.wsattr(bool, default=False, name='hot-config')
    """On-the-fly configuration support."""

    priority = wtypes.wsattr(int)
    """Priority of the extension."""

    @classmethod
    def sample(cls):
        sample = cls(name='example',
                     description='Sample extension.',
                     enabled=True,
                     hot_config=False,
                     priority=2)
        return sample
