from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes

class Monochrome(Base):
    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = colors.neutral,
        secondary_hue: colors.Color | str = colors.neutral,
        neutral_hue: colors.Color | str = colors.neutral,
        spacing_size: sizes.Size | str = sizes.spacing_lg,
        radius_size: sizes.Size | str = sizes.radius_md,
        text_size: sizes.Size | str = sizes.text_md,
        font: fonts.Font
        | str
        | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("Arvo"),
            "ui-serif",
            "system-ui",
            "serif",
        ),
        font_mono: fonts.Font
        | str
        | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("IBM Plex Mono"),
            "ui-monospace",
            "Consolas",
            "monospace",
        ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        self.name = "monochrome"
        super().set(
            # # Colors
            # body_text_color="*neutral_900",
            # block_label_text_color="c",
            # block_title_text_color="*body_text_color",
            body_text_color_subdued="*body_text_color",
            # background_fill_primary_dark="*neutral_900",
            # background_fill_secondary_dark="*neutral_800",
            # block_background_fill_dark="*neutral_800",
            input_background_fill_dark="*neutral_900",
            button_primary_background_fill_dark="*neutral_900",
            button_primary_text_color_dark="pink",
            # # Borders
            # block_border_width="0px",
            # block_border_width_dark="1px",
            # shadow_drop_lg="0 1px 4px 0 rgb(0 0 0 / 0.1)",
            # block_shadow="*shadow_drop_lg",
            # block_shadow_dark="none",
            # # Block Labels
            # block_title_text_weight="600",
            block_label_text_size="*text_lg",
        )