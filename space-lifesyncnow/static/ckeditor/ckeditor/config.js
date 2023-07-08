/**
 * @license Copyright (c) 2003-2023, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function (config) {
    // Define changes to default configuration here. For example:
    // config.language = 'fr';
    // config.uiColor = '#AADC6E';

    // --------- custom class for image2 plugin
    config.extraPlugins = "image2";

    // Apply the responsive class to images
    config.image2_responsive = true;
    // this css class "ck-image-responsive is in the ckeditor.css inside static", but i am giving this class in my react project because the frontend code is rendering there
    config.image2_responsiveClass = "ck-image-responsive";
    // --------- custom class for image2 plugin
};
