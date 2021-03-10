(require 'package)
(add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/") t)
(package-initialize)

(global-visual-line-mode)

;; 1. makes sure the file ~/.emacs does not exist. (look out for that "dot" at the front)

;; 2. make sure that the directory ~/.emacs.d/ DOES exist; create it if necessary
;; and watch all those dots.

;; 3. After that put this file in ~/.emacs.d/

;; 4. Restart emacs and make sure you see NO ERROR MESSAGES or warning.

;; 5. Then look at "readme" in this directory for further instructions. 

;; (use-package magit
;;   :ensure t
;;   :bind ("C-c m" . magit-status)
;;   )
