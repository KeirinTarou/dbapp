"use strict";

{

    $(function() {
        const $textarea = $('#sql_query');

        $textarea.on('keydown', function(e) {
            if (e.key === "Tab") {
                e.preventDefault();
                // テキストエリア内の選択範囲の位置を取得
                const start = this.selectionStart;
                const end = this.selectionEnd;
                const value = this.value;

                if (e.shiftKey) {
                    // Shift + Tab: 直前にタブ文字があれば削除
                    if (value.substring(start - 1, start) === "\t") {
                        this.value = value.substring(0, start - 1) + value.substring(end);
                        this.selectionStart = this.selectionEnd = start - 1;
                    }
                } else {
                    // Tab: タブ追加
                    this.value = value.substring(0, start) + "\t" + value.substring(end);
                    this.selectionStart = this.selectionEnd = start + 1;
                }
                this.selectionStart = this.selectionEnd = start + 1;
            }
        }); 
    });

}